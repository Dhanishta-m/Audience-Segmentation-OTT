def get_recommendation(cluster):

    recommendations = {

        0: {
            "segment": "Casual Viewers",
            "content": [
                "Trending Movies",
                "Short Movies",
                "Comedy Shows"
            ]
        },

        1: {
            "segment": "Movie Lovers",
            "content": [
                "Drama Movies",
                "Romantic Movies",
                "Classic Films"
            ]
        },

        2: {
            "segment": "Premium Engaged Users",
            "content": [
                "New Releases",
                "Original Series",
                "Premium Content"
            ]
        },

        3: {
            "segment": "Binge Watchers",
            "content": [
                "Web Series",
                "Long Movies",
                "Popular Series"
            ]
        }
    }


    return recommendations.get(
        cluster,
        {
            "segment":"Unknown",
            "content":[]
        }
    )