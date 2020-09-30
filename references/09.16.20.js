// get count of all documents in the collection
Jokes.countDocuments().then((num) => {
    // Get a random entry
    const randomNum = Math.floor(Math.random() * num);

    // grab random document
    Jokes.findOne()
        .skip(randomNum)
        .then((joke) => {
            // send results
            res.json({ results: joke });

            // catch error
        })
        .catch((err) => {
            // err msg
            res.json({
                message: 'An error has occurred.',
                error: err,
            });
        });
});
