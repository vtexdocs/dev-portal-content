const fs = require('fs');
const path = require('path');
const sdk = require('api')('@developers/v2.0#nysezql0wwo236');
require('dotenv').config()

const docsDir = path.join(__dirname, '..', 'docs')
const notesDir = path.join(docsDir, 'release-notes')

const createDir = (dir) => {
  if (!fs.existsSync(dir)) {
    fs.mkdirSync(dir)
  }
}


const getNotes = async (rootDir, apikey) => {
  sdk.auth(apikey);
  if (!fs.existsSync(rootDir)) {
    fs.mkdirSync(rootDir);
  }
  let pageNumber = 0;
  let result = [], notes = [];
  do {
    result = result.concat(notes);
    pageNumber++;
    notes = await sdk.getChangelogs({ perPage: 100, page: pageNumber });
  } while(notes.length !== 0);

  return result;
}

const sortNotes = (resultRest, resultDevelopers) => {
  let i = 0, j = 0;
  const result = [];
  while(i < resultRest.length || j < resultDevelopers.length) {
    if(i == resultRest.length) {
      result.push(resultDevelopers[j])
      j++;
    } else if (j == resultDevelopers.length) {
      result.push(resultRest[i]);
      i++;
    } else if (resultRest[i].createAt === resultDevelopers[j].createAt) {
      result.push(resultDevelopers[j]);
      i++;
      j++;
    } else if (resultRest[i].createAt > resultDevelopers[j].createAt) {
      result.push(resultRest[i]);
      i++;
    } else {
      result.push(resultDevelopers[j])
      j++;

    }
  }
  return result;
}

const createFrontMatter = ((metadata, releaseNote) => {
  let frontMatter = '---\n'
  metadata.forEach(data => {
    const stringsType = ['title', 'slug', 'type'];
    const isString = stringsType.includes(data);
    const metaDataValue = isString ? releaseNote[data].replace(/"/g, '\\"') : releaseNote[data]
    frontMatter += `${data}: ${isString ? '"': ''}${metaDataValue}${isString ? '"': ''}\n`
  })
  return frontMatter + '---\n\n'
})

const createNotes = async (rootDir, restAPIKEY, devPortalAPIKEY) => {
  const dirs = [docsDir, notesDir]
  dirs.forEach((dir) => createDir(dir))

  const resultRest = await getNotes(rootDir, restAPIKEY);
  const resultDevelopers = await getNotes(rootDir, devPortalAPIKEY);

  const sorteredResult = sortNotes(resultRest, resultDevelopers);
  sorteredResult.forEach((releaseNote) => {
    const releaseNotePath = path.join(rootDir, `${releaseNote.slug}.md`);
    const frontMatterTemplate = ['slug', 'title', 'createdAt', 'hidden', 'type'];
    const frontMatter = createFrontMatter(frontMatterTemplate, releaseNote);

    fs.appendFileSync(releaseNotePath, frontMatter + releaseNote.body);
  })
}

createNotes(notesDir, process.env.REST_API_KEY, process.env.DEVPORTAL_API_KEY);
