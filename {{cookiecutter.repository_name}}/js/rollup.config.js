import resolve from "rollup-plugin-node-resolve";
import commonjs from "rollup-plugin-commonjs";
import replace from "rollup-plugin-replace";

export default {
  input: "src/index.js",
  output: {
    file: "../{{cookiecutter.python_package_name}}/bundle.js",
    format: "esm",
  },
  plugins: [
    resolve(),
    commonjs(),
    replace({
      "process.env.NODE_ENV": JSON.stringify("production"),
    }),
  ],
};
