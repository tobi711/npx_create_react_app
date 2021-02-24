import React, {useState,useEffect} from 'react'; 

import './App.css';

function App() {

  const [currentTime, setCurrentTime] = useState(0);
  useEffect(() => {
    fetch('/time').then(res => res.json()).then(data=> {
      setCurrentTime(data.time); 
    })
  }, []); 

  const[initalData, setInitialData] = useState([{}]); 
  useEffect(() => {
    fetch('/data').then(
      response => response.json()
    ).then(data => setInitialData(data))
  },[]);


  return (
    <div className="App">
      <h1> {initalData.Message}</h1>
      <h1><p> ALL: {initalData.all_visitor} </p></h1>
      <h1><p>MSS1: {initalData.mss1_left_side} </p></h1>
      <h1><p> MSS3: {initalData.mss3_right_side} </p></h1>
      <h1><p> ALL unique Macs: </p>{initalData.all_unique_macs}</h1>
      <h1><p> MAcs inside: {initalData.macs_inside} </p></h1>
      <h1><p> MSS2 Inside: {initalData.mss2_inside} </p></h1>
      <h1><p> procent: {initalData.procent_visitors} </p></h1>
    </div>
  );

}

export default App;
