const fs = require('fs')
const path = require('path')
const frontmatter = require('front-matter')
const imageDownloader = require('image-downloader')

const baseURL = 'https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main'
const rootDir = path.resolve(__dirname, '..')

const getExtension = (url) => {
  let dotIndex = url.length - 1
  while (dotIndex >= 0 && url[dotIndex] !== '.') {
    dotIndex--
  }

  if (dotIndex < 0) return 'png'
  return url.substring(dotIndex + 1)
}

const updateImages = async (filepath) => {
  const content = fs.readFileSync(filepath, 'utf-8')
  const slug = frontmatter(content).attributes.slug
  
  const images = []
  const newContent = content.replace(
    /\!\[(.*)\]\((.*)\)/g,
    (match, altText, url) => {
      if (url.startsWith(baseURL)) return match

      if (url.startsWith('http://') || url.startsWith('https://')) {
        const ext = getExtension(url)
        const filename = `${slug}-${images.length}.${ext}`
  
        images.push({
          filepath: path.resolve('images', filename),
          url
        })

        return `![${altText}](${baseURL}/images/${filename})`
      }

      if (path.isAbsolute(url)) {
        return `![${altText}](${baseURL}${url})`
      }

      const imagePath = path.resolve(path.dirname(filepath), url).replace(rootDir, '')
      return `![${altText}](${baseURL}${imagePath})`
    }
  )

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
