import { useEffect, useState } from "react"
import axios from "axios"

import NewsCard from "./components/NewsCard"

function App() {

  const [articles, setArticles] = useState([])
  const [loading, setLoading] = useState(true)
  const [topic, setTopic] = useState("technology")

  useEffect(() => {

    fetchNews(topic)

  }, [])

  const fetchNews = async (searchTopic) => {

    setLoading(true)

    try {

      const response = await axios.get(
        `https://ai-based-news-chatbot-1.onrender.com/news?topic=${searchTopic}`
      )

      setArticles(response.data)

    } catch (error) {

      console.log(error)

    } finally {

      setLoading(false)

    }

  }

  const handleSearch = () => {

    fetchNews(topic)

  }

  return (

    <div className="min-h-screen bg-slate-100">

      {/* Navbar */}

      <div className="bg-white shadow-sm border-b">

        <div className="max-w-7xl mx-auto px-6 py-5 flex justify-between items-center">

          <h1 className="text-4xl font-bold text-slate-800">
            AI News Chatbot
          </h1>

          <div className="flex gap-4">

            <input
              type="text"
              placeholder="Search news..."
              value={topic}
              onChange={(e) => setTopic(e.target.value)}
              className="px-5 py-3 rounded-xl border border-slate-300 w-80 outline-none focus:ring-2 focus:ring-blue-500 text-black"
            />

            <button
              onClick={handleSearch}
              className="bg-blue-600 text-white px-6 py-3 rounded-xl hover:bg-blue-700 transition"
            >
              Search
            </button>

          </div>

        </div>

      </div>

      {/* Categories */}

      <div className="max-w-7xl mx-auto px-6 py-6 flex flex-wrap gap-4">

        {
          ["technology", "sports", "business", "health", "entertainment", "ai", "bitcoin"]
          .map((category) => (

            <button
              key={category}
              onClick={() => {
                setTopic(category)
                fetchNews(category)
              }}
              className="bg-white border border-slate-300 px-5 py-2 rounded-full hover:bg-blue-600 hover:text-white transition"
            >
              {category}
            </button>

          ))
        }

      </div>

      {/* News */}

      <div className="max-w-7xl mx-auto px-6 pb-10">

        {
          loading ?

          (
            <h2 className="text-center text-2xl text-slate-700 mt-20">
              Loading News...
            </h2>
          )

          :

          (
            <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">

              {
                articles.map((article, index) => (

                  <NewsCard
                    key={index}
                    article={article}
                  />

                ))
              }

            </div>
          )
        }

      </div>

    </div>

  )
}

export default App