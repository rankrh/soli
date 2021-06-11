
export const Row = ({ children }) => {
    return (
        <div className="row mb-3">
            { children }
        </div>
    );
}

function getColumnSize(sizes) {
    let classes = "col ";

    return classes;
}

export const Column = ({ children, sizes }) => {

    const classes = getColumnSize(sizes);

    return (
        <div className={ classes }>
            { children }
        </div>
    );
}