import { useState } from "react";
import axios from "axios";
import "./App.css";


function App() {

  const [user, setUser] = useState({
    Age: "",
    PreferredGenre: "Action",
    WatchHours: "",
    LoginPerWeek: "",
    CompletionRate: ""
  });


  const [result, setResult] = useState(null);


  const handleChange = (e) => {

    setUser({
      ...user,
      [e.target.name]: e.target.value
    });

  };


  const analyzeUser = async () => {

    try {

      const response = await axios.post(
        "http://127.0.0.1:5000/predict",
        {
          ...user,
          Age:Number(user.Age),
          WatchHours:Number(user.WatchHours),
          LoginPerWeek:Number(user.LoginPerWeek),
          CompletionRate:Number(user.CompletionRate)
        }
      );


      setResult(response.data);

    }

    catch(error){

      console.log(error);
      alert("Backend not connected");

    }

  };


  return (

    <div className="container">

      <h1>🎬 OTT Audience Segmentation</h1>


      <div className="card">


        <input
          name="Age"
          placeholder="Age"
          onChange={handleChange}
        />


        <select
          name="PreferredGenre"
          onChange={handleChange}
        >

          <option>Action</option>
          <option>Comedy</option>
          <option>Drama</option>
          <option>Horror</option>
          <option>Romance</option>
          <option>Sci-Fi</option>

        </select>


        <input
          name="WatchHours"
          placeholder="Watch Hours"
          onChange={handleChange}
        />


        <input
          name="LoginPerWeek"
          placeholder="Login Per Week"
          onChange={handleChange}
        />


        <input
          name="CompletionRate"
          placeholder="Completion Rate %"
          onChange={handleChange}
        />


        <button onClick={analyzeUser}>
          Analyze User
        </button>


      </div>



      {
        result &&

        <div className="result">

          <h2>Audience Segment</h2>

          <h3>
            🔥 {result.segment}
          </h3>


          <h2>
            Recommended Content
          </h2>


          {
            result.recommendations.map(
              (item,index)=>
              <p key={index}>
                🎥 {item}
              </p>
            )
          }


        </div>

      }


    </div>

  )

}


export default App;