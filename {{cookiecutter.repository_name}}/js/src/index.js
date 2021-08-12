import React from "react";
import ReactDOM from "react-dom";
import htm from "htm";

const html = htm.bind(React.createElement);

export function bind(node, config) {
  return {
    create: (type, props, children) => React.createElement(type, props, ...children),
    render: (element) => ReactDOM.render(element, node),
    unmount: () => ReactDOM.unmountComponentAtNode(node),
  }
}

export function ExampleCounter(props) {
  const [count, setCount] = React.useState(0);

  const updateCount = () => {
    const newCount = count + 1;
    props.onCountChange(newCount);
    setCount(newCount);
  };

  return html`<div>
    <button id=${props.buttonId} onClick=${updateCount}>
      ${props.buttonText}
    </button>
    <p>current count is: ${count}</p>
  </div>`;
}
