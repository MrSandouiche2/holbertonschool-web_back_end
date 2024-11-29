export default function getResponseFromAPI() {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve('Data received from API');
    }, 2000);

    reject(new Error('API error'));
  });
}
