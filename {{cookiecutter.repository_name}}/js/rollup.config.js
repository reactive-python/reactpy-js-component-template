import resolve from "rollup-plugin-node-resolve";
import commonjs from "rollup-plugin-commonjs";

var packageJSON = require("./package.json");

var externals = {
  resolveId(source) {
    if (packageJSON.peerDependencies && packageJSON.peerDependencies[source]) {
      return { id: `./${source}.js`, external: true };
    } else {
      return null;
    }
  },
};

export default {
  input: "src/index.js",
  output: {
    file: "../{{cookiecutter.python_package_name}}/bundle.js",
    format: "esm",
  },
  plugins: [externals, resolve(), commonjs()],
};
