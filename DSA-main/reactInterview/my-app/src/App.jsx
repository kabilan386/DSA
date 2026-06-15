import { useState } from 'react'
import './App.css'
import  {mockApi}  from './api'
import { useTheme } from './ThemeContex';

function App() {
  const { theme, toggleTheme } = useTheme();
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
      <h1>Current Theme: {theme}</h1>
      <button onClick={toggleTheme}>
        Toggle Theme
      </button>
     </div>

    <div className={`app-container ${theme}`}>
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
