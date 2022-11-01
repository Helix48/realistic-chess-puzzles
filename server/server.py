from flask import Flask, request
from mongoContext import randomFen, gameQuantity
from evaluate import evaluation
from lichessContext import fetchLichessGames

app = Flask(__name__)


@app.route("/api/engineEvaluation/<encodedFen>", methods=["GET"])
async def getEngineEvaluation(encodedFen):
    fen = encodedFen.replace('\\', '/')
    analysis = await evaluation(fen)
    return analysis


@app.route("/api/database/randomFen", methods=["GET"])
async def getRandomFen():
    moveFilter = request.args.get('moveFilter')
    ratingRange = request.args.get('ratingRange')
    fenData = await randomFen(moveFilter, ratingRange)
    return fenData


@app.route("/api/database/gameQuantity", methods=["GET"])
async def getGameQuantity():
    moveFilter = request.args.get('moveFilter')
    ratingRange = request.args.get('ratingRange')
    return {"quantity": gameQuantity(moveFilter, ratingRange)}


@app.route("/api/lichess/randomLichessGame", methods=["GET"])
async def randomLichessGame():
    user = request.args.get('user')
    max = request.args.get('max')
    redoFens = await fetchLichessGames(user, max)
    print(redoFens)
    return {"redoFens": redoFens}

if __name__ == "__main__":
    app.run(debug=True)
