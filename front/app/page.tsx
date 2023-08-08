import SearchBar from '@/components/search-bar';
import styles from '../styles/home.module.scss';
import SearchResult from '@/components/search-result';

export default function Home() {
  return (
    <main className={styles['main']}>
      
      <SearchBar/>

      <SearchResult/>

    </main>
  )
}
