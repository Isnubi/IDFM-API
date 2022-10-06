<a name="readme-top"></a>

<!-- Projet Shields -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- Replace these markers with infos - "IDFM-API"-->

<div align="center">


<h3 align="center">RER B informations viewer</h3>
  <p align="center">
    <a href="https://github.com/Isnubi/IDFM-API/"><strong>Explore the docs »</strong></a>
    <br />--------------------
    <br />
    <a href="https://github.com/Isnubi/IDFM-API/issues">Report Bug</a>
    ·
    <a href="https://github.com/Isnubi/IDFM-API/issues">Request Feature</a>
  </p>
</div>


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This project is a simple viewer for RER B informations. It uses the Ile de France Mobilités REST API to get the informations and display them using Flask.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Python][Python-shield]][Python-url]
* [![Flask][Flask-shield]][Flask-url]
* [![JSON][JSON-shield]][JSON-url]
* [![HTML][HTML-shield]][HTML-url]
* [![CSS][CSS-shield]][CSS-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started
<a name="getting-started"></a>

You can install **this project** by following these steps.

### Prerequisites

1. Clone the repository on your computer.

    ```sh
    git clone https://github.com/Isnubi/IDFM-API.git
    cd IDFM-API
    ```
   
   * If **Git** is not installed, you can install it from [here](https://git-scm.com/downloads) or 
   download the repository as a zip file from [here](https://github.com/Isnubi/IDFM-API/archive/refs/heads/master.zip)
        ```sh
        sudo apt install git
        ```

2. Install **Python**. You can download it [here](https://www.python.org/downloads/) or by using the following command on Linux:

   * Debian/Ubuntu:
     ```sh
     sudo apt install python3 python3-pip
     ```
  
   * Fedora/CentOS/RHEL:
     ```sh
     sudo dnf install python3 python3-pip
     ```

3. Install the required python packages using **pip**:

    ```sh
    python3 -m pip install -r requirements.txt
    ```
   If the requirements.txt file didn't work, you can install the required packages manually using the following command:
    ```sh
    python3 -m pip install flask requests beautifulsoup4 pdf2image
    ```

### Installation

1. Get an API Key at [https://prim.iledefrance-mobilites.fr/](https://prim.iledefrance-mobilites.fr/fr)
2. Enter your API Key in `private/config.py`
    ```
    token = "YOUR_API_KEY"
    ```
3. Run the flask application
    ```sh
   flask --app app.py run
   ```


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

The application is accessible at [http://localhost:5000/](http://localhost:5000/).

You have an index page with button to access the different pages:
- **Home**: The home page
- **Trafic**: The trafic infos page
- **Horaires**: The schedules page
- **Plan**: The map page


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] Add a map page

See the [open issues](https://github.com/Isnubi/IDFM-API/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.md` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact


Isnubi - [@Louis_Gambart](https://twitter.com/Louis_Gambart) - [contact@louis-gambart.fr](mailto:louis-gambart.fr)
<br>**Discord:** isnubi#6221

**Project Link:** [https://github.com/Isnubi/IDFM-API](https://github.com/Isnubi/IDFM-API)

<p align="right">(<a href="#readme-top">back to top</a>)</p>




<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/Isnubi/IDFM-API.svg?style=for-the-badge
[contributors-url]: https://github.com/Isnubi/IDFM-API/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Isnubi/IDFM-API.svg?style=for-the-badge
[forks-url]: https://github.com/Isnubi/IDFM-API/network/members
[stars-shield]: https://img.shields.io/github/stars/Isnubi/IDFM-API.svg?style=for-the-badge
[stars-url]: https://github.com/Isnubi/IDFM-API/stargazers
[issues-shield]: https://img.shields.io/github/issues/Isnubi/IDFM-API.svg?style=for-the-badge
[issues-url]: https://github.com/Isnubi/IDFM-API/issues
[license-shield]: https://img.shields.io/github/license/Isnubi/IDFM-API.svg?style=for-the-badge
[license-url]: https://github.com/Isnubi/IDFM-API/blob/master/LICENSE.md
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/louis-gambart
[Python-shield]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/
[JSON-shield]: https://img.shields.io/badge/JSON-5E5C5C?style=for-the-badge&logo=json&logoColor=white
[JSON-url]: https://www.json.org/json-en.html
[HTML-shield]: https://img.shields.io/badge/HTML-E34F26?style=for-the-badge&logo=html5&logoColor=white
[HTML-url]: https://html.spec.whatwg.org/multipage/
[CSS-shield]: https://img.shields.io/badge/CSS-1572B6?style=for-the-badge&logo=css3&logoColor=white
[CSS-url]: https://www.w3.org/Style/CSS/Overview.en.html
[Flask-shield]: https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white
[Flask-url]: https://flask.palletsprojects.com/en/2.0.x/
[Twitter-shield]: https://img.shields.io/twitter/follow/Louis_Gambart?style=social
[Twitter-url]: https://twitter.com/Louis_Gambart/