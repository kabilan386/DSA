export const  mockApi = {
  fetchMock: (category) => {

    console.log("1. Promise started");

    new Promise((resolve) => {

      setTimeout(() => {
        console.log("4. Promise resolved after 2 sec");
        resolve();
      }, 2000);

    });

    console.log("2. Database executing immediately");

    const database = {
      Electronic: [
        { id: 1, name: "Laptop", price: 50000 },
        { id: 2, name: "Mobile", price: 20000 },
      ],
    };

    console.log("3. Returning data immediately");

    return database[category] || [];
  },
};