from models.models import User, Address

def get_users(request):
    limit = request.args.get('limit', None)
    order_by = request.args.get('order_by', None)
    filter_obj = {}

    for key in request.args:
        if key not in ['limit', 'order_by']:
            filter_obj[key] = request.args[key]

    users = User.query.filter_by(**filter_obj).order_by(order_by).limit(limit).all()

    return users

def create_user(db, body):
    user = User.from_json(body)
    db.session.add(user)
    db.session.commit()
    address = Address.from_json(body['address'], user.id)
    db.session.add(address)
    db.session.commit()

    return user

def update_user(db, user, body):
    user.name = body.get('name', user.name)
    user.age = body.get('age', user.age)
    if 'address' in body:
        user.address.street = body['street'].get('street', user.address.street)
        user.address.number = body['number'].get('number', user.address.number)
        user.address.city = body['city'].get('city', user.address.city)
        user.address.state = body['state'].get('state', user.address.state)
    db.session.commit()

def delete_user(db, user):
    db.session.delete(user)
    db.session.commit()