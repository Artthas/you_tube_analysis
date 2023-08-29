'use client';

import { Dispatch, ReactNode, createContext, useReducer } from "react";

type SearchResult = {
  main_channel: {
    channel_name: string[],
    top_new: string[],
    top_popular: string[],
    main_description: string,
    main_keys: string,
    ideas_by_top_new: Idea[],
    ideas_by_top_popular: Idea[]
  },
  concurrent_channels: {
    channel_name: string[],
    top_new: string[],
    top_popular: string[],
    ideas_by_top_new: Idea[],
    ideas_by_top_popular: Idea[]
  }
}

type Idea = {
  'Main Title': string,
  'Alternative Title 1': string,
  'Alternative Title 2': string,
  'Description': string
}

type ContextProps = {
  children: ReactNode;
}

type ContextState = {
  searchResult: SearchResult;
  isResultLoading: boolean;
  isResultLoadingError: boolean;
};

type ContextAction = {
  type: string;
  payload: any;
};

const initialState: ContextState = {
  searchResult: {
    main_channel: {
      channel_name: [],
      top_new: [],
      top_popular: [],
      main_description: '',
      main_keys: '',
      ideas_by_top_new: [],
      ideas_by_top_popular: []
    },
    concurrent_channels: {
      channel_name: [],
      top_new: [],
      top_popular: [],
      ideas_by_top_new: [],
      ideas_by_top_popular: []
    }
  },
  isResultLoading: false,
  isResultLoadingError: false,
};

const reducer = (state: ContextState, action: ContextAction) => {
  switch (action.type) {
    case "SET_SEARCH_RESULT":
      return { ...state, searchResult: action.payload };
    case "SET_IS_RESULT_LOADING":
      return { ...state, isResultLoading: action.payload };
    case "SET_IS_RESULT_LOADING_ERROR":
      return { ...state, isResultLoadingError: action.payload };
    default:
      return state;
  }
};

export const GlobalContext = createContext<{
  state: ContextState;
  dispatch: Dispatch<ContextAction>;
}>({
  state: initialState,
  dispatch: () => null
});

export const GlobalContextProvider = ({children}: ContextProps) => {
  const [state, dispatch] = useReducer(reducer, initialState);

  return (
    <GlobalContext.Provider value={{ state, dispatch }}>
      {children}
    </GlobalContext.Provider>
  );
};
