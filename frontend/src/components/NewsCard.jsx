import { useState } from "react"
import axios from "axios"

function NewsCard({ article }) {

  const [summary, setSummary] = useState("")
  const [loading, setLoading] = useState(false)

  const summarizeNews = async () => {

    setLoading(true)

    try {

      const response = await axios.post(
        "https://ai-based-news-chatbot-1.onrender.com/summarize",
        {
          text: `
          Title: ${article.title}

          Description: ${article.description}
          `
        }
      )

      setSummary(response.data.summary)

    } catch (error) {

      console.log(error)

    } finally {

      setLoading(false)

    }

  }

  return (

    <div className="bg-white rounded-2xl overflow-hidden shadow-md hover:shadow-xl transition duration-300">

      <img
        src={article.image}
        alt="news"
        className="w-full h-56 object-cover"
      />

      <div className="p-5">

        <h2 className="text-xl font-bold text-slate-800 mb-3">
          {article.title}
        </h2>

        <p className="text-slate-600 mb-4">
          {article.description}
        </p>

        <p className="text-sm text-slate-400 mb-4">
          {article.source}
        </p>

        <div className="flex gap-3 flex-wrap">

          <a
            href={article.url}
            target="_blank"
            className="bg-blue-600 text-white px-5 py-2 rounded-lg hover:bg-blue-700 no-underline"
          >
            Read More
          </a>

          <button
            onClick={summarizeNews}
            className="bg-green-600 text-white px-5 py-2 rounded-lg hover:bg-green-700"
          >
            {
              loading
              ? "Summarizing..."
              : "AI Summary"
            }
          </button>

        </div>

        {
          summary && (

            <div className="bg-slate-100 p-4 rounded-xl mt-5">

              <h3 className="font-bold text-slate-800 mb-2">
                AI Summary
              </h3>

              <p className="text-slate-700 whitespace-pre-line">
                {summary}
              </p>

            </div>

          )
        }

      </div>

    </div>

  )
}

export default NewsCard