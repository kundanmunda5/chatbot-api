app:  git(repo)
    ver_1:
        src/ :
            main_chat_body_with_redis_connection.py : with redis and timeout

        utils/ : 
            redis_server.py
            required_dependencies.py : 
            requirement.py 
            user_session_timeout.py
            chat_completions.py

        data/ :
            
        dir/ stock_recommendations : 
            hot_trending_stocks.py
            long_term_growth_stocks.py
            recommend_me_some.py
            sector_wise_stock_recommend.py
            stock_information.py
            top_gainers*.py

        services/ :
            top_performance_api.py : calling external apis from UAT,refinitive  to recommend the stocks
        
        faqs/ : Storing Appreciate FAQs
            Appreciate FAQs Doc.docx

        test_scripts:

            low_grwoth_recommend.ipynb
            Chatbot.ipynb

api:


dir/ stock_recommendations

