
USE InvODS;
GO

SET NOCOUNT ON;

-- ====================================================================================================
-- Drop/Create Function: dbo.fnRemoveNonNumericChars
--
-- Author:		Eric Bragas - DesignMind
-- Created:		9/1/2016
-- Description: Removes alpha characters from strings which should only contain numbers
-- ====================================================================================================

-- ====================================================================================================
-- Cleanup
-- ====================================================================================================

IF OBJECT_ID('dbo.fnRemoveNonNumericChars', 'FN') IS NOT NULL
	BEGIN
		DROP FUNCTION dbo.fnRemoveNonNumericChars;
		PRINT CONVERT(VARCHAR(20), GETDATE(), 120) + ' : Dropped Function, dbo.fnRemoveNonNumericChars.';
	END;
GO

-- ====================================================================================================
-- Create Function
-- ====================================================================================================

CREATE FUNCTION fnRemoveNonNumericChars ( @strText VARCHAR(1000) )
RETURNS VARCHAR(1000)
AS
	BEGIN
		WHILE PATINDEX('%[^0-9.]%', @strText) > 0
			BEGIN
				SET @strText = STUFF(@strText, PATINDEX('%[^0-9.]%', @strText), 1, '');
			END;
		RETURN @strText;
	END;
GO

PRINT CONVERT(VARCHAR(20), GETDATE(), 120) + ' : Created Function, dbo.fnRemoveNonNumericChars.';
GO