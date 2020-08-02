<h1 align="center">agine <br>
<a href="https://github.com/ZenithClown/agine/blob/master/LICENSE"><img alt="GitHub license" src="https://img.shields.io/github/license/ZenithClown/agine?style=plastic"></a>
<a href="https://twitter.com/intent/tweet?text=Wow:&url=https%3A%2F%2Fgithub.com%2FZenithClown%2Fagine"><img alt="Twitter" src="https://img.shields.io/twitter/url?label=dPramanik&logo=linkedin&style=plastic&url=https%3A%2F%2Fwww.linkedin.com%2Fin%2Fdpramanik%2F"></a>
</h1>

<p align="justify"><i>agine</i> is a Python package which have functionalities related to points in an n-dimensional space (which is defined by its <code>x, y, ...z</code> coordinates), or an actual position on the Earth (given by its <code>latitude, longitude</code>). Considering two points (<code>say P, Q</code>), apart from many other purposes, this library can also detect if the two have a clear line of sight or not. <br>
  <b>NOTE:</b> this package comes with IPython-Notebooks (in <code>docs</code>) which is there to explain some basic stuffs and functionalities related to this library.
</p>

## Basic Usage

<p align="justify">agine has <b>three</b> main functionalities: (1) Calculation of Distances, using different metrics, which is defined under <code>commons</code>, (2) Functions to Find the Nearest Neighbor and (3) Function to Find if two Geographic Point has a <i>Line-of-Sight</i> or not. All of this can be done using the following:</p>

```python
pip install -e agine # Installing agine with pip
import agine

	>> Setting up agine-Environment...
	>>   Detected OS            : "<os-name-with-version>"
	>>   scikit-learn Options   : "<is-scikit-learn-available>"
	>>   "etc. which Defines the Core-Capability"
```

<p align="justify">agine has a hard dependency of only <code>numpy</code> so that some of its functionalities can be used somewhere else. For options (2) and (3) it has different requirements, which can be accessed using: <code>agine.OSOptions._point_func</code> and <code>agine.OSOptions._line_of_st</code> repectively.</p>
