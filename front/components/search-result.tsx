'use client';

import React, { useContext } from 'react';
import { GlobalContext } from '@/context';
import styles from '../styles/components/search-result.module.scss';

export default function SearchResult() {

  const { state: { searchResult } } = useContext(GlobalContext);

  console.log(searchResult);

  return (
    <div>
      
    </div>
  )
}
