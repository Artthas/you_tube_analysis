type DispatchType = (action: { type: string, payload: any }) => void;
type MockDataType = { final_json: any };

export const simulateReqServer = (dispatch: DispatchType, mockData: MockDataType) => {
  const { final_json } = mockData;
  dispatch({ type: 'SET_SEARCH_RESULT', payload: {
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
  } });
  dispatch({ type: 'SET_IS_RESULT_LOADING', payload: true });
  setTimeout(() => {
      dispatch({ type: 'SET_IS_RESULT_LOADING', payload: false });
      dispatch({ type: 'SET_SEARCH_RESULT', payload: final_json });
  }, 1000);
}