module.exports = {
    devServer: {
      proxy: {
        '/api': {
          target: 'http://127.0.0.1:5000', //proxy prema server aplikaciji
          ws: true,
          changeOrigin: true,
          pathRewrite: {
            '^/api': ''
          }
        }
      }
    }
  };