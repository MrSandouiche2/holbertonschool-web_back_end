/** @type {import('eslint').Linter.FlatConfig} */
const airbnbConfig = require('eslint-config-airbnb-base');  // Importer la config Airbnb
const importPlugin = require('eslint-plugin-import');      // Importer le plugin import

const config = [
  {
    files: ['*.js'],  // Spécifie les fichiers JS
    languageOptions: {
      ecmaVersion: 2021,  // Version ECMAScript
      sourceType: 'module', // Type de source (module)
    },
    plugins: {
      import: importPlugin  // Utilisation du plugin 'import' comme objet
    },
    rules: {
      ...airbnbConfig.rules,  // Applique les règles d'Airbnb
    },
  },
];

module.exports = config;  // Exporte la configuration
