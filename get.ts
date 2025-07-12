import { walk } from "jsr:@std/fs";

const foldername = "src/resume_ai_copilot";
let conetents = "";

for await (const entry of walk(foldername)) {
  if (entry.isFile && entry.name.endsWith(".py")) {
    const fileContent = await Deno.readTextFile(entry.path);
    conetents += `// File: ${entry.path}\n${fileContent}\n\n`;
  }
}

const outputFile = "output.txt";
await Deno.writeTextFile(outputFile, conetents);