import React from 'react';
import { RecoilRoot } from 'recoil';
// import { RootStore } from 'stores';
import { Router } from './Router';

import './styles/global.scss';

// const rootStore = new RootStore() as any;

export const App = () => {
  return (
    <RecoilRoot>
      <Router />
    </RecoilRoot>
  );
};

export default App;
