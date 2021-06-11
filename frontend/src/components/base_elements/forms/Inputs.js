
export const Text = ({ placeholder, maxlength, required }) => {

    return <input type="text" class="form-control" placeholder={ placeholder } maxlength={ maxlength } required={ required } />
}

export const Select = ({ placeholder, required, children }) => {
    return(
        <select name="species" class="custom-select font-italic" placeholder={ placeholder } required={ required }>
            { children }
        </select>
    );
}

export const Option = ({ name, value, selected }) => {
    return <option value={ value } selected={ selected }>{ name }</option>;
}

export const TextArea = ({ placeholder, dimensions }) => {
    return (
        <textarea class="form-control" cols={ dimensions[0] } rows={ dimensions[1] }  placeholder={ placeholder }/>
    );
    }