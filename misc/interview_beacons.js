import { useState } from "react";

/*This task is meant to be ambiguous and a bit poorly defined. 
Every sentence in this prompt is intentional and contains a necessary
product requirement that must be satisfied.

In this exercise, we will work on a cat picture feed. Each picture in 
the feed will also have a text field for the user to enter a note for 
each picture. You should keep the state of the picture URL and the note 
together (imagine that it was coming from a SQL read). (If this is 
confusing, definitely ask for clarification.) The feed will start 
empty and the user should have the ability to add more cat pictures 
to the feed. For example, if there are currently two cat pictures, 
and I add another, there should now be three cat pictures in total shown.
 
To add a picture to the feed, we will perform a GET request from 
https://aws.random.cat/meow which returns a JSON {file: image_url} 
with a random image. The initial note for each picture will start off 
empty but should be editable any time after. 
 
I'm not looking for the UI to be anything special because this exercise 
is not a test of your UI intuition, but it should definitely be usable. 
Use inline styling. We will code only in App.js, so do not 
make new files. You may use any libraries that you wish. The allotted 
time for this exercise is 30 minutes. Choose wisely where you want to 
spend your time. We are pair programming and I can help answer your 
questions and I will fix some of your small typos to help the app compile.

Prooduct Requirements:
- cat picture feed
- text field for the user to enter a note for each picture
- https://aws.random.cat/meow which returns a JSON {file: image_url} 

*You should keep the state of the picture URL and the note together (imagine that it was coming from a SQL read)
*/

const apiUrl = "https://thatcopy.pw/catapi/rest/";
// const apiUrl = "https://aws.random.cat/meow";

export default function App() {
  const [collection, setCollection] = useState([]);
  const fetchPicture = async () => {
    const res = await fetch(apiUrl).then((v) => v.json());
    setCollection((state) => state.concat([{ img: res.webpurl, note: "" }]));
  };

  const updateNote = (idx) => (e) => {
    collection[idx] = { ...collection[idx], note: e.target.value };
    const newState = [...collection];
    setCollection(newState);
  };

  return (
    <div className="App">
      <h1>Cat Pictures</h1>
      <div>
        {collection.map((cat, idx) => (
          <CatCard key={idx} onChange={updateNote(idx)} {...cat} />
        ))}
      </div>
      <button onClick={fetchPicture}>Fetch new Cat</button>
    </div>
  );
}

const CatCard = ({ img, note, onChange }) => (
  <div>
    <img src={img} style={{ height: "320px" }} />
    <input type="text" value={note} {...{ onChange }} />
  </div>
);
