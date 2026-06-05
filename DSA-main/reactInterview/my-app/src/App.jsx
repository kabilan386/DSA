import { useState } from 'react'
import './App.css'
import  {mockApi}  from './api'


function App() {
  
  const [data, setData] = useState([]);

  const handleClick = async () => {

    console.log("Button clicked");

    const result =
      await mockApi.fetchMock("Electronic");

    console.log("5. Result received", result);

    setData(result);
  };

  return (
    <>
     <div>

      <button onClick={handleClick}>
        Load Data
      </button>

      {data.map((item) => (
        <p key={item.id}>
          {item.name}
        </p>
      ))}

    </div>
    </>
  )
}

export default App
