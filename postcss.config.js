// postcss.config.js
module.exports = {
  plugins: [
    require('postcss-import'),   // ← This handles @import merging
    require('cssnano')({         // ← This minifies the final CSS
      preset: 'default',
    }),
  ],
};
