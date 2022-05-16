const fs = require('fs');
const path = require('path');
const sdk = require('api')('@developers/v2.0#nysezql0wwo236');
require('dotenv').config()

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

const createNotes = async (rootDir, apiKey1, apiKey2) => {
  const resultRest = await getNotes(rootDir, apiKey1);
  const resultDevelopers = await getNotes(rootDir, apiKey2);

  const sorteredResult = sortNotes(resultRest, resultDevelopers);
  sorteredResult.forEach((releaseNote) => {
    const releaseNotePath = path.join(rootDir, `${releaseNote.slug}.md`);
    const frontMatterTemplate = ['slug', 'title', 'createdAt', 'hidden', 'type'];
    const frontMatter = createFrontMatter(frontMatterTemplate, releaseNote);

    fs.appendFileSync(releaseNotePath, frontMatter + releaseNote.body);
  })
}

createNotes(path.join(__dirname, '..', 'docs', 'release-notes'), process.env.REST_API_KEY, process.env.DEVPORTAL_API_KEY);
