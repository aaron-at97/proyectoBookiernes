from django.views.generic import TemplateView
from eBook.auth_views import LoginView
from django.urls import path
from django.conf.urls import url
from eBook.books_view import BooksList, BookCreate
from eBook.image_view import BooksImageList, BooksPublishList
from eBook.views import rolsStaff, notifyEs, notifyEd, notifyDis, notifyMaq, editorsChief, disenyChief

urlpatterns = [
    url(r'^$', LoginView.as_view(), name="login"),
    path('list_books/', BooksList.as_view(), name="list_book"),
    path('book_create/', BookCreate.index, name='book_create'),
    path('book_create/save', BookCreate.procesar_formulario, name='book_createSave'),
    path('book_publish/', editorsChief.as_view(), name="book_publish"),
    path('book_acept/', TemplateView.as_view(template_name='books/editor/libros_aceptados.html'), name="book_acept"),
    path('book_rejected/', TemplateView.as_view(template_name='books/editor/libros_rechazados.html'), name='book_rejected'),
    path('index/', rolsStaff.as_view(), name='rolsbook'),

    path('book_publish/asignedEditor/', TemplateView.as_view(template_name='books/editor/asignar_editor.html'), name='asignedEd'),
    path('book_publish/rejectBook/', TemplateView.as_view(template_name='books/editor/rechazar_libror.html'), name='rejectBook'),
    path('book_publish/motiveReject/', TemplateView.as_view(template_name='books/escritor/motivo_rechazo.html'), name='motiveReject'),
    path('book_publish/motiveReject/', TemplateView.as_view(template_name='books/escritor/motivo_rechazo.html'), name='motiveReject'),

    path('book_image/list_books_image', BooksImageList.as_view(), name="list_book_image"),
    path('book_image/push_diseny', TemplateView.as_view(template_name='books/diseñador/push_diseny.html'), name='push_diseny'),
    path('book_image/asign_diseny', disenyChief.as_view(), name="asign_diseny"),
    path('book_image/asign_disenyPop', TemplateView.as_view(template_name='books/diseñador/asignar_popUp.html'), name='push_disenyPopUp'),

    path('book_publish/list_books_publish', BooksPublishList.as_view(), name="list_book_publish"),
    path('book_publish/subir_libro', TemplateView.as_view(template_name='books/maquetador/publish_book.html'), name="subir_libro"),
    path('book_publish/book_publicate', TemplateView.as_view(template_name='books/maquetador/book_publicate.html'), name="book_publicate"),

    path('book_image/rev_img', TemplateView.as_view(template_name='books/editor/rev_img.html'), name="revImg"),
    path('book_image/sol_img', TemplateView.as_view(template_name='books/editor/solicitud_img.html'), name="solImg"),
    path('book_image/ver_img', TemplateView.as_view(template_name='books/editor/ver_imagenes.html'), name="ver_img"),
    path('book_image/reject_bookBatery', TemplateView.as_view(template_name='books/editor/rechazar_solicitudImg.html'), name="rejectBookBatery"),

    path('notifyEd/', notifyEs.as_view(), name='notifyEs'),
    path('notifyEs/', notifyEd.as_view(), name='notifyEd'),
    path('notifyDis/', notifyDis.as_view(), name='notifyDis'),
    path('notifyMaq/', notifyMaq.as_view(), name='notifyMaq'),
]
