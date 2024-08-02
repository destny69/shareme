import { combineReducers } from "redux";
import { fileListReducer } from './fileReducers'


export default combineReducers ({
    fileList: fileListReducer,

});

