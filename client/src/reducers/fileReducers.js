import axios from 'axios';
import {
    FILE_LIST_REQUEST,
    FILE_LIST_SUCCESS,
    FILE_LIST_FAIL 
} from '../actions/types'

export const fileListReducer = (
    state = {
        files: [],
        loading: false,
    }, 
    action
) => {
    switch (action.type){
        case FILE_LIST_REQUEST:
            return {
                loading:true, files : []
            };
        case FILE_LIST_SUCCESS:
            return  {
                loading:false,
                files: action.payload.result
            };
        case FILE_LIST_FAIL:
                return {
                    loading:false,
                    error: action.payload
                    
                }
        default:
            return state;
    }
};
