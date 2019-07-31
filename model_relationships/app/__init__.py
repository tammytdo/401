from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app(ConfigClass):
    app = Flask(__name__)
    app.config.from_object(ConfigClass)
    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():

        ##   Chocolate CRUD    #####################

        @app.route("/chocolates", methods=["GET"])
        def all_chocolates():
            chocolates = [chocolate.to_dict() for chocolate in Chocolate.query.all()]
            
            return jsonify(chocolates)

        @app.route("/chocolates/<int:id>")
        def one_band(id):
            chocolate = Chocolate.query.get(id)
            
            return jsonify(chocolate.to_dict())

        @app.route("/chocolates", methods=["POST"])
        def create_band():
            chocolate_info = request.json or request.form
            chocolate = Chocolate(name=chocolate_info.get("name"))
            db.session.add(chocolate)
            db.session.commit()

            return jsonify(chocolate.to_dict())

        @app.route("/chocolates/<int:id>", methods=["PUT"])
        def update_chocolate(id):
            chocolate_info = request.json or request.form
            chocolate_id = Chocolate.query.filter_by(id = id).update(chocolate_info)
            db.session.commit()
            
            return jsonify(chocolate_id)

        @app.route("/chocolates/<int:id>", methods=["DELETE"])
        def delete_chocolate(id):
            chocolate = Chocolate.query.get(id)
            db.session.delete(chocolate)
            db.session.commit()
            
            return jsonify(id)

        @app.route("/chocolates/<string:name>", methods=["GET"])
        def get_band_by_name(name):
            chocolate = Chocolate.query.filter_by(name=name).first()
            
            return jsonify(chocolate.to_dict())

        ##   Brand CRUD  #####################

        @app.route("/brand", methods=["GET"])
        def all_artists():
            brands = [artist.to_dict() for brand in Brand.query.all()]
            
            return jsonify(brand)

        @app.route("/brand/<int:id>")
        def one_brand(id):
            brand = Brand.query.get(id)
            
            return jsonify(brand.to_dict())

        @app.route("/brand", methods=["POST"])
        def create_brand():
            brand_info = request.json or request.form
            brand = Brand(
                name = brand_info.get("name"), chocolate_id = brand_info.get("chocolate")
            )
            db.session.add(brand)
            db.session.commit()
            
            return jsonify(brand.to_dict())

        @app.route("/brand/<int:id>", methods=["DELETE"])
        def delete_brand(id):
            brand = Brand.query.get(id)
            db.session.delete(brand)
            db.session.commit()
            
            return jsonify(id)

        @app.route("/brand/<int:id>", methods=["PUT"])
        def update_brand(id):
            brand_info = request.json or request.form
            brand_id = Brand.query.filter_by(id=id).update(brand_info)
            db.session.commit()
            
            return jsonify(brand_id)

        @app.route("/chocolates/<int:id>/brand")
        def get_brand_in_chocolate(id):
            brand = [brand.to_dict() for brand in Chocolate.query.get(id).brand]
            
            return jsonify(brand)

        return app


from app.models import Chocolate, Brand