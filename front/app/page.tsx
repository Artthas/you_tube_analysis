import SearchBar from '@/components/search-bar';
import SearchResult from '@/components/search-result';
import styles from '../styles/home.module.scss';

export default function Home() {
  return (
    <main className={styles['main']}>
      
      <SearchBar/>

      <SearchResult/>

    </main>
  )
}
