import { PrimaryButton } from "../buttons/button";

export const InputGroup = ({ children }) => {
    
    return (
        <div class="col input-group">
            { children }
        </div>
    );
}

export const ButtonAppend = () => {
    return (
        <div class="input-group-append">
            <PrimaryButton value="Add New"></PrimaryButton>
        </div>
    );
}

export const InputGroupText = ({ value }) => {
    return (
        <span class="input-group-text">{ value }</span>
    );
}