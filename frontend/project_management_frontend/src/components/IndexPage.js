import React from 'react';
import { Link } from 'react-router-dom';
import managementImg from '../assets/management.png';

function IndexPage () {
  console.log('IndexPage component Mounted');

  return (
    <div className='index-page'>
      <header className='hero-header' style={{ backgroundImage: `url(${managementImg})`  }}>
      </header>

      <div className='sidebar'>
        <ul>
          <li><Link to='/login'>Login</Link></li>
          <li><Link to='/signup'>Sign Up</Link></li>
            <li><a href='#get-started'>Get Started</a></li>
          </ul>
        </div>

      
          <section id='about'>
              <h3>About Echelon</h3>
              <p>Echelon is a simplified project management tool with amazing user experience and ease of use.</p>
              <p>The inspiration came from our own struggles while we try to navigate project management tools and often times we have to use the tutorial to understand how to navigate. This made us think of building a simple tool with minimal features which someone with limited to no computer literacy skills could use to manage their projects.</p>
            
          </section>

          <section id='team'>
            <h3>Our Team</h3>
            <ul>
              <li>Timothy Ngungi</li>
              <li>Austin Morara</li>
              <li>Purity Okumu</li>
            </ul>
          </section>
        
      
      <footer>
        <p>&copy; 2024 Echelon. All rights reserved.</p>
      </footer>
    </div>
  );
}

export default IndexPage;
