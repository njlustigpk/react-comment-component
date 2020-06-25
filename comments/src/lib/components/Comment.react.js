import React, {Component} from 'react';
import PropTypes from 'prop-types';

/**
 * ExampleComponent is an example component.
 * It takes a property, `label`, and
 * displays it.
 * It renders an input with the property `value`
 * which is editable by the user.
 */
export default class Comment extends Component {
    render() {
        const {id, setProps, value, className} = this.props;

        return (
            <div id={id} className={className}>
                <textarea onChange={e=>setProps({value:e.target.value})}>
                    {value}
                </textarea>
            </div>
        );
    }
}

Comment.defaultProps = {};

Comment.propTypes = {
    /**
     * The ID used to identify this component in Dash callbacks.
     */
    id: PropTypes.string.isRequired,


    /**
     * The value displayed in the input.
     */
    value: PropTypes.string,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,

    /**
     * className to select div with CSS
     */
    className: PropTypes.string
};
