from sqlalchemy.orm import Session

import models
import schemas


def get_all_authors(db: Session) -> list[models.DBAuthor]:
    return db.query(models.DBAuthor).all()


def get_author(db: Session, author_id: int) -> models.DBAuthor:
    return db.query(models.DBAuthor).filter(models.DBAuthor.id == author_id).first()


def create_author(db: Session, author: schemas.AuthorCreate) -> models.DBAuthor:
    db_author = models.DBAuthor(
        name=author.name,
        bio=author.bio
    )
    db.add(db_author)
    db.commit()
    db.refresh(db_author)

    return db_author


def get_all_books(db: Session, book: schemas.BookCreate) -> list[models.DBBook]:
    return db.query(models.DBBook).all()


def get_book_by_author_id(db: Session, author_id: int) -> list[models.DBBook]:
    if author_id:
        query = db.query(models.DBBook).filter(models.DBBook.author_id == author_id)
    return query.all()


def create_book(db: Session, book: schemas.BookCreate) -> models.DBBook:
    db_book = models.DBBook(
        title=book.title,
        summary=book.summary,
        publication_date=book.publication_date,
        author_id=book.author_id
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book