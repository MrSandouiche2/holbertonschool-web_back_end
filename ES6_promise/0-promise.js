export default function getResponseFromAPI() {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      const success = true;
      if (success) {
        resolve('Data received from API');
      } else {
        reject(new Error('API error'));
      }
    }, 1000);
  });
}
