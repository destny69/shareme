import axios from 'axios';
import {
    FILE_LIST_REQUEST,
    FILE_LIST_SUCCESS,
    FILE_LIST_FAIL 
} from './types'


export const listfiles = () => async (dispatch) => {
    try {
        dispatch({
            type: FILE_LIST_REQUEST,
            payload: {}

        })
        const {data} = await axios.get("/api/v1/share-file/")

        dispatch({
            type: FILE_LIST_SUCCESS,
            payload: data
            })
        }
    
    catch (error) {
        dispatch({
            type: FILE_LIST_FAIL,
            payload: error.response && error.response.data.message ? error.response.data.message : error.message,


    })
}
};