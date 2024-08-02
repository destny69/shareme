import { applyMiddleware, createStore } from "redux";
import { composeWithDevTools } from "redux-devtools-extension";
import { thunk as reduxThunk } from 'redux-thunk'; // Correct import for redux-thunk
import rootReducer from './reducers';

// Define the initial state of the application
const initialState = {};

// Define the middleware to be used (redux-thunk for handling asynchronous actions)
const middleware = [reduxThunk];

// Create the Redux store with the root reducer, initial state, and middleware
const store = createStore(
    rootReducer,
    initialState,
    composeWithDevTools(applyMiddleware(...middleware))
);

// Export the store for use in the application
export default store;
