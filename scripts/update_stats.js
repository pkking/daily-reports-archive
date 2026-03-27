const fs = require('fs');
const { execSync } = require('child_process');

const dataPath = './public/data.json';
let historyData = [];
if (fs.existsSync(dataPath)) {
  historyData = JSON.parse(fs.readFileSync(dataPath, 'utf8'));
}

console.log('Fetching recent runs...');
const rawOutput = execSync('gh run list --workflow="Send Daily Reports via Email" --json databaseId,status,conclusion,createdAt,url --limit 30').toString();
const recentRuns = JSON.parse(rawOutput);

const historyMap = new Map(historyData.map(run => [run.databaseId, run]));
recentRuns.forEach(run => historyMap.set(run.databaseId, run));

const mergedData = Array.from(historyMap.values()).sort((a, b) => new Date(b.createdAt) - new Date(a.createdAt));

if (!fs.existsSync('./public')) fs.mkdirSync('./public');
fs.writeFileSync(dataPath, JSON.stringify(mergedData, null, 2));
console.log(`Updated stats. Total runs: ${mergedData.length}`);
