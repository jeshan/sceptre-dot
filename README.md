Helps you visualise your Sceptre projects with Graphviz (DOT).

![screenshot.png](https://github.com/jeshan/sceptre-dot/screenshot.png)

# Benefits
- Visualisation can be added as a documentation artefact to your project
- Having many explicit/implicit dependencies can slow down deployments. Use the generated dependency graph to quickly spot bottlenecks due to these dependencies. 

# Installation

Install graphviz for your operating system as per [official instuctions](https://graphviz.gitlab.io/download/).

Install this package in the same python interpreter (virtualenv) that Sceptre is installed so that its python library is already available:
`pip install sceptre-dot`

# Usage
In the same directory where you would normally invoke `sceptre launch -y $YOUR_PATH`, run: 

```bash
sceptre-dot $YOUR_PATH > output.dot
fdp -Tpng output.dot -o output.png # use fdp engine for best results
```



Released under the Simplified BSD Licence.
