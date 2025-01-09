saveOutput(code, outputFile) {
    const fs = require('fs');
    
    fs.writeFileSync(outputFile, code);
    console.log(`Translated code saved to ${outputFile}`);
}