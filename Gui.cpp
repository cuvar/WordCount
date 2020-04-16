#include <windows.h>

//Prototypen
LRESULT CALLBACK WindowProc (HWND hWnd, UINT message,
							 WPARAM wParam, LPARAM lParam);

HWND ErstelleHauptfenster (HINSTANCE hInst);
void ErstelleSteuerelemente (HWND hWnd, HINSTANCE hInst);

//IDs der Child-Fenster
#define ID_STATICTEXT      4000
#define ID_EDITBOX         4001
#define ID_BTN_UEBERNEHMEN 4002
#define ID_BTN_BEENDEN     4003

//Globale Variablen
HWND hText;
HWND hEditBox;
HWND hUebernehmen;
HWND hBeenden;

//Hauptprogramm
int WINAPI WinMain (HINSTANCE hInst, HINSTANCE hPrevInst,
					LPSTR lpcmdline, int ncmdshow)
{
	HWND hWnd;
	MSG message;

	hWnd = ErstelleHauptfenster (hInst);

	//Prüfen, ob alles glattging
	if (hWnd == NULL)
		return (0);

	ErstelleSteuerelemente (hWnd, hInst);

	//Der "Herzschlag" des Programms
	//Hier werden alle Nachrichten abgeholt,
	//übersetzt und weitergeleitet
	//
	while (GetMessage (&message, NULL, 0, 0) )
	{
		TranslateMessage (&message);
		DispatchMessage  (&message);

	}

	// Programm beenden
	return (int)(message.wParam);

} 



// Hauptfenster erstellen und Handle zurückliefern
//
HWND ErstelleHauptfenster (HINSTANCE hInst)
{
	HWND        hWnd;        // Fenster-Handle
	WNDCLASSEX  windowclass; // Nachricht

	// Der Klassenname des Fensters ist frei w�hlbar
	const TCHAR szClassName[] = TEXT("Zweites Fenster");

	// Struktur mit gew�nschten Eigenschaften f�llen
	//

	//Größe der Struktur zwischenspeichern
	windowclass.cbSize = sizeof (WNDCLASSEX);

	//Fenster soll beim Verschieben neu gezeichnet werden
	windowclass.style = CS_HREDRAW | CS_VREDRAW;

	//Zeiger auf Callback-Funktion
	windowclass.lpfnWndProc = WindowProc;

	//Keine erweiterten Einstellungen
	windowclass.cbClsExtra = 0;
	windowclass.cbWndExtra = 0;

	windowclass.hInstance = hInst;

	windowclass.hIcon   = LoadIcon (NULL, IDI_APPLICATION);
	windowclass.hIconSm = LoadIcon (NULL, IDI_APPLICATION);
	windowclass.hCursor = LoadCursor (NULL, IDC_ARROW);

	windowclass.hbrBackground = (HBRUSH)COLOR_BACKGROUND+1;

	windowclass.lpszMenuName = NULL;

	//Klassenname angeben
	windowclass.lpszClassName = szClassName;

	//Fensterklasse registrieren
	if (!RegisterClassEx (&windowclass) )
		return (NULL);

	//Fenster erzeugen
	hWnd = CreateWindowEx (NULL,
		szClassName,
		TEXT("WordCount"),
		WS_OVERLAPPEDWINDOW | WS_VISIBLE,
		CW_USEDEFAULT, CW_USEDEFAULT,
		600, 400,
		NULL,
		NULL,
		hInst,
		NULL);

	// Fensterhandle zurückgeben
	return (hWnd);

}


// Alle Steuerelemente erstellen
//
void ErstelleSteuerelemente (HWND hWnd, HINSTANCE hInst)
{
	hText = CreateWindow (TEXT("STATIC"),
						  TEXT("Eingegebener Text"),
						  WS_VISIBLE | WS_CHILD | ES_CENTER,
						  0, 0,
						  300, 20,
						  hWnd,
						  (HMENU)ID_STATICTEXT,
						  hInst,
						  NULL);

	hEditBox = CreateWindow (TEXT("EDIT"),
							 TEXT("Bitte Text eingeben"),
							 WS_VISIBLE | WS_CHILD | WS_BORDER,
							 0, 20,
							 300, 20,
							 hWnd,
							 (HMENU)ID_EDITBOX,
							 hInst,
							 NULL);

	hUebernehmen = CreateWindow (TEXT("BUTTON"),
								 TEXT("Uebernehmen"),
								 BS_PUSHBUTTON | WS_VISIBLE | WS_CHILD,
								 20, 50,
								 95, 40,
								 hWnd,
								 (HMENU)ID_BTN_UEBERNEHMEN,
								 hInst,
								 NULL);

	hBeenden = CreateWindow (TEXT("BUTTON"),
							 TEXT("Beenden"),
							 BS_PUSHBUTTON | WS_VISIBLE | WS_CHILD,
							 175, 50,
							 95, 40,
							 hWnd,
							 (HMENU)ID_BTN_BEENDEN,
							 hInst,
							 NULL);

}

// Callback-Funktion zur Nachrichtenverarbeitung
//
LRESULT CALLBACK WindowProc (HWND hWnd, UINT message,
							 WPARAM wParam, LPARAM lParam)
{
	// Messages auswerten
	switch (message)
	{
		//Fenster schlie�en? (Auch Alt-F4)
		case WM_DESTROY:
		{
			//Nachricht zum Beenden schicken
			PostQuitMessage (0);
			return (0);

		}

		//Ab hier die Nachrichten unserer Child-Fenster bearbeiten
		case WM_COMMAND:
		{
			switch (wParam)
			{
				case ID_BTN_UEBERNEHMEN:
				{
					TCHAR szText[256];

					GetWindowText (hEditBox, szText, 256);

					SetWindowText (hText, szText);
					SetWindowText (hEditBox, TEXT(""));

					return (0);

				}

				case ID_BTN_BEENDEN:
				{
					int Resultat;

					// Messagebox für Sicherheitsabfrage
					Resultat = MessageBox (hWnd, TEXT("Wirklich beenden?"),
						TEXT("Programm beenden"),
						MB_YESNO | MB_ICONQUESTION);

					if (Resultat == IDYES)
					{
						PostQuitMessage (0);
						return (0);

					}

					return (0);

				}
			} break;
		} break;
	}

	// Die Nachricht wurde nicht von uns verarbeitet, also
	// von Windows verarbeiten lassen
	return (DefWindowProc (hWnd, message, wParam, lParam) );

} // WindowProc
