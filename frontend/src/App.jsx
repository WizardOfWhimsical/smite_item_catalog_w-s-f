import { useState, useEffect } from "react";
import "./App.css";

const connectionString = "/v1/api/py_backend";

function App() {
  const [test, setTest] = useState("");

  useEffect(() => {
    async function get_fetch() {
      const resp = await fetch(connectionString);
      if (!resp.ok) {
        console.log("data not ok");
      }
      const data = await resp.json();
      console.log("data", data.message);
      setTest(data.message);
    }
    get_fetch();
  }, [test]);

  return (
    <>
      <h1>{test}</h1>
    </>
  );
}

export default App;
