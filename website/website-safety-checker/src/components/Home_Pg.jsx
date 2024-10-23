// import React, { useState } from 'react';
// import axios from 'axios'; 

// const Home_Pg = () => {
//   const [url, setUrl] = useState('');
//   const [result, setResult] = useState('');

//   const handleSubmit = async (e) => {
//     e.preventDefault();
//     // Mocking an API call here, replace with my actual API call
//     if (url.includes('https')) {
//       setResult('Safe');
//     } else {
//       setResult('Unsafe');
//     }
//   };

//   return (
//     <div className="checker-container">
//       <form onSubmit={handleSubmit}>
//         <label htmlFor="urlInput">Enter Website URL:</label>
//         <input
//           type="text"
//           id="urlInput"
//           value={url}
//           onChange={(e) => setUrl(e.target.value)}
//           placeholder="https://example.com"
//           required
//         />
//         <button type="submit">Check Safety</button>
//       </form>

//       {result && (
//         <div className={`result ${result === 'Safe' ? 'safe' : 'unsafe'}`}>
//           <h3>{`The website is ${result}`}</h3>
//         </div>
//       )}
//     </div>
//   );
// };

// export default Home_Pg;

// 2
import React, { useState } from "react";

const Home_Pg = () => {
  const [url, setUrl] = useState('');
  const [result, setResult] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    // Mocking an API call here, replace with actual API call
    if (url.includes('https')) {
      setResult('Safe');
    } else {
      setResult('Unsafe');
    }
  };

  return (
    <div className="app-container">
      {/* Left white portion */}
      <div className="left-container">
        <div className="app-header">
          ML Enhanced WebApp Firewall
        </div>
        <div className="checker-container">
          <form onSubmit={handleSubmit}>
            <label htmlFor="website-url">Enter Website URL:</label>
            <input
              type="text"
              id="website-url"
              value={url}
              onChange={(e) => setUrl(e.target.value)}
              placeholder="https://example.com"
              required
            />
            <button type="submit">Check Safety</button>
          </form>

          {result && (
            <div className={`result ${result === 'Safe' ? 'safe' : 'unsafe'}`}>
              <h3>{`The website is ${result}`}</h3>
            </div>
          )}
        </div>
      </div>

      {/* Right black portion for video or blank space */}
      <div className="right-container">
        {/* <video autoPlay loop muted playsInline>
          <source src="your-video.mp4" type="video/mp4" />
          Your browser does not support the video tag.
        </video> */}
      </div>
    </div>
  );
};

export default Home_Pg;
