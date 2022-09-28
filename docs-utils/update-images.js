const fs = require('fs')
const path = require('path')
const frontmatter = require('front-matter')
const imageDownloader = require('image-downloader')

const baseURL = 'https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main'
const rootDir = path.resolve(__dirname, '..')

const isValidExtension = (ext) => {
  return /^[a-zA-Z0-9]*$/.test(ext)
}

const getExtension = (url) => {
  let dotIndex = url.length - 1
  while (dotIndex >= 0 && url[dotIndex] !== '.') {
    dotIndex--
  }

  const ext = url.substring(dotIndex + 1)
  if (dotIndex < 0 || !isValidExtension(ext)) return 'png'
  return ext
}

const updateImages = async (filepath) => {
  const content = fs.readFileSync(filepath, 'utf-8')
  const slug = frontmatter(content).attributes.slug
  
  const images = []
  const replaceURL = (match, extra, url) => {
    const isMarkdownBlock = match.startsWith('![')
    if (url.startsWith(baseURL)) return match

    let newURL = ''
    if (url.startsWith('http://') || url.startsWith('https://')) {
      const ext = getExtension(url)
      const filename = `${slug}-${images.length}.${ext}`
  
      images.push({
        filepath: path.resolve('images', filename),
        url
      })

      newURL = `${baseURL}/images/${filename}`
    } else if (path.isAbsolute(url)) {
      newURL = `${baseURL}${url}`
    } else {
      newURL = `${baseURL}${path.resolve(path.dirname(filepath), url).replace(rootDir, '')}`
    }

    return isMarkdownBlock ? `![${extra}](${newURL})` : `<img ${extra}src="${newURL}"`
  }

  const newContent = content
    .replace(/\!\[(.*)\]\((.*)\)/g, replaceURL)
    .replace(/<img (.*)src="(.*)"/g, replaceURL)

  try {
    for (let i = 0; i < images.length; i++) {
      await imageDownloader.image({
        url: images[i].url,
        dest: images[i].filepath
      })
    }
  
    fs.writeFileSync(filepath, newContent)
  } catch (err) {
    console.log("Couldn't download some of the images, leaving file as it is...")
  }
}

const filepath = process.argv[2]
updateImages(filepath)
