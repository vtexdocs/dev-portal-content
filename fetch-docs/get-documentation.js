const fs = require('fs')
const path = require('path')
const yaml = require('yaml')
require('dotenv').config()

const sdk = require('api')('@developers/v2.0#nysezql0wwo236')

const docsDir = path.join(__dirname, '..', 'docs')
const guidesDir = path.join(docsDir, 'guides')
const referenceDir = path.join(docsDir, 'reference')
const vtexIODir = path.join(docsDir, 'vtex-io')

const createDir = (dir) => {
  if (!fs.existsSync(dir)) {
    fs.mkdirSync(dir)
  }
}

const getMarkdownBody = (doc) => {
  const frontMatter = yaml.stringify({
    title: doc.title,
    category: doc.category,
    hidden: doc.hidden,
    order: doc.order,
    parentDoc: doc.parentDoc
  })

  const body = `---\n${frontMatter}---\n${doc.body}`

  return body;
}

const getDoc = async (dir, docSlug) => {
  const docDir = path.join(dir, docSlug)
  createDir(docDir)

  const fetchDoc = async (attempts) => {
    try {
      const doc = await sdk.getDoc({ slug: docSlug })

      const body = getMarkdownBody(doc)

      console.log(`Fetched document ${docSlug}`)
    } catch (e) {
      if (attempts < 10) {
        console.log(`Failed to fetch ${docSlug}. Retrying...`)
        setTimeout(() => fetchDoc(attempts + 1), attempts * 10)
      } else {
        console.log(`Failed to fetch ${docSlug}`)
      }
    }
  }

  await fetchDoc(1)
}

const getDocs = async (dir, categorySlug) => {
  const categoryDir = path.join(dir, categorySlug)
  createDir(categoryDir)

  const docs = await sdk.getCategoryDocs({ slug: categorySlug })
  for (let i = 0; i < docs.length; i++) {
    const { children, slug } = docs[i]
    await getDoc(categoryDir, slug)

    for (let j = 0; j < children.length; j++) {
      await getDoc(path.join(categoryDir, slug), children[j].slug)
    }
  }

  console.log(`Fetched documents from ${categorySlug}`)
}

const getCategories = async (apiKey, dirs) => {
  sdk.auth(apiKey)

  let page = 1
  let categories = []

  do {
      categories = await sdk.getCategories({ perPage: 100, page })
      for (let i = 0; i < categories.length; i++) {
        const { slug, type } = categories[i]
        if (type in dirs) {
          await getDocs(dirs[type], slug)
        }
      }

      page++
  } while (categories.length !== 0)
}

const getDocumentation = async () => {
  const dirs = [docsDir, guidesDir, referenceDir, vtexIODir]
  dirs.forEach((dir) => createDir(dir))

  await getCategories(process.env.REST_API_KEY, { guide: guidesDir, reference: referenceDir })
  await getCategories(process.env.DEVPORTAL_API_KEY, { guide: vtexIODir })
}

getDocumentation()
